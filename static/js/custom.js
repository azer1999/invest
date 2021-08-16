try {
    for (let valute of document.getElementsByClassName('single-currency-select')) {
        valute.addEventListener('click',()=>{
            for (let toBeRemoved of document.getElementsByClassName('single-currency-select')) {
                toBeRemoved.classList.remove('selected-currency');
                toBeRemoved.classList.remove('active');
            }

            valute.classList.add('selected-currency');
            valute.classList.add('active');

            document.getElementsByClassName('displayed-selected-currency')[0].textContent = valute.textContent

            if (valute.textContent == 'USD') {
                document.getElementById('basic-addon1').textContent = '$';
            }

            if (valute.textContent == 'AZN') {
                document.getElementById('basic-addon1').textContent = '₼';
            }

            if (valute.textContent == 'EUR') {
                document.getElementById('basic-addon1').textContent = '€';
            }

        })
    }
} catch (error) {
    console.log();
}



try {
    document.getElementById('toggle_edit_credentials').addEventListener('click',()=>{

        for (let crcrdntl of document.getElementsByClassName('current_credential')) {
            crcrdntl.classList.toggle('active')
        }

        for (let edcrdntl of document.getElementsByClassName('editable_credential')) {
            edcrdntl.classList.toggle('active')
        }

    })
} catch (error) {
    document.write()
}
