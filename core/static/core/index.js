document.addEventListener('DOMContentLoaded', () => {
    // call initial function
    title = document.getElementsByClassName('active-screener')[0].innerText
    clause = document.getElementsByClassName('active-clause')[0].innerText
    setInterval(() => {
        updateData(title, clause)
    }, 34000)
})

function updateData(title, clause) {
    fetch(`/get_data/${title}/${clause}`, {
        method: 'POST', 
    })
    .then(response => response.json())
    .then(res => {
        const tbody = document.getElementById('mytable').getElementsByTagName('tbody')[0];
        tbody.innerHTML = ''
        for (let i = 0; i < res.length; i++) {
            let row = document.createElement('tr')
            let content = `<tr class="stock-row border-b2">
                <td scope="row" class="px-6 py-4 font-medium text-gray-900 whitespace-nowrap dark:text-white">
                    ${res[i]['nsecode']}
                </td>
                <td class="px-6 py-4">
                    <a href="https://www.tradingview.com/chart/?symbol=NSE%3A${res[i]['nsecode']}" target="_blank" class="font-medium text-blue-600 dark:text-blue-500 hover:underline">${res[i]['name']}</a>
                </td>
                <td class="px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white">
                    ${res[i]['per_chg']}
                </td>
                <td class="px-6 py-4 text-gray-900 whitespace-nowrap dark:text-white">
                    ${res[i]['close']}
                </td>
            </tr>`;
            row.innerHTML = content
            if (i % 2 != 0) {
                let classes = "bg-gray-50 dark:bg-gray-700".split(' ');
                row.classList.add(...classes)
            } else {
                let classes = "bg-white dark:bg-gray-800".split(' ');
                row.classList.add(...classes)
            }
            tbody.append(row)
        }
    })
}
