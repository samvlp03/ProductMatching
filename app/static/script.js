document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('barcode-form');
    const resultDiv = document.getElementById('result');
    const tableBody = document.getElementById('scanned-products-body');
    const productDetailsDiv = document.getElementById('product-details');
    const productCategory = document.getElementById('product-category');
    const productModelNo = document.getElementById('product-model-no');
    const productPartNo = document.getElementById('product-part-no');
    const productSerialNo = document.getElementById('product-serial-no');
    const serialNoInput = document.getElementById('serial_no');
    const partNoInput = document.getElementById('part_no');

    serialNoInput.focus();

    serialNoInput.addEventListener('input', () => {
        setTimeout(() => {
            if (serialNoInput.value.trim() !== '') {
                partNoInput.focus();
            }
        }, 150); // Delay of 150ms
    });

    partNoInput.addEventListener('input', async () => {
        setTimeout(async () => {
            if (partNoInput.value.trim() !== '') {
                const formData = new FormData(form);
                const response = await fetch(form.action, {
                    method: 'POST',
                    body: formData,
                });

                const data = await response.json();
                console.log('Response Data:', data); // Debugging log

                // Clear existing table rows
                tableBody.innerHTML = '';

                if (data.status === 'ok') {
                    resultDiv.textContent = 'OK';
                    resultDiv.style.color = 'green';

                    productCategory.textContent = data.product.category;
                    productModelNo.textContent = data.product.model_no;
                    productPartNo.textContent = data.product.part_no;
                    productSerialNo.textContent = data.product.serial_no;
                    productDetailsDiv.style.display = 'block';
                } else if (data.status === 'ng') {
                    resultDiv.textContent = 'NG';
                    resultDiv.style.color = 'red';
                    productDetailsDiv.style.display = 'none';
                } else if (data.status === 'already_scanned') {
                    resultDiv.textContent = 'Already Scanned';
                    resultDiv.style.color = 'orange';
                    productDetailsDiv.style.display = 'none';

                    data.scanned_products.forEach(product => {
                        const row = document.createElement('tr');
                        row.innerHTML = `<td>${product.model_no}</td><td>${product.serial_no}</td><td>${product.part_no}</td>`;
                        tableBody.appendChild(row);
                    });
                } else {
                    console.error('Unknown status:', data.status); // Debugging log for unknown status
                }

                form.reset();
                serialNoInput.focus(); // Return focus to the SerialNo input for the next scan
            }
        }, 150); // Delay of 150ms
    });
});

function printSerialNumber(serialNumber) {
    // Create an image element for the barcode
    const barcodeImage = document.createElement('img');

    // Generate the barcode for Serial Number using JsBarcode
    JsBarcode(barcodeImage, serialNumber, {
        format: "CODE128", // You can change the barcode format if needed
        width: 2,
        height: 100,
        displayValue: true // Show the serial number below the barcode
    });

    // Open a new window for printing
    const printWindow = window.open('', '', 'height=400,width=600');
    printWindow.document.write('<html><head><title>Print Serial Number</title></head><body>');

    // Add the barcode image to the print window
    printWindow.document.body.appendChild(barcodeImage);

    printWindow.document.write('</body></html>');
    printWindow.document.close();

    // Print the barcode
    printWindow.onload = function () {
        printWindow.print();
    };
}

function printPartNumber(partNumber) {
    // Create an image element for the barcode
    const barcodeImage = document.createElement('img');

    // Generate the barcode for Part Number using JsBarcode
    JsBarcode(barcodeImage, partNumber, {
        format: "CODE128", // You can change the barcode format if needed
        width: 2,
        height: 100,
        displayValue: true // Show the part number below the barcode
    });

    // Open a new window for printing
    const printWindow = window.open('', '', 'height=400,width=600');
    printWindow.document.write('<html><head><title>Print Part Number</title></head><body>');

    // Add the barcode image to the print window
    printWindow.document.body.appendChild(barcodeImage);

    printWindow.document.write('</body></html>');
    printWindow.document.close();

    // Print the barcode
    printWindow.onload = function () {
        printWindow.print();
    };
}

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
