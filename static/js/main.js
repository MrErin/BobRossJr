console.log('loaded')

document.getElementById('js-clicker').addEventListener('click', () => {
fetch('http://127.0.0.1:8000/birthday')
  .then(response => {
    return response.json();
  })
  .then(birthdays => {
    console.log(JSON.stringify(birthdays));
    b_list = document.getElementById('b_list')
    birthdays.forEach(birthday => {
        let el = document.createElement('li')
        el.textContent = `Today is ${birthday.date}, which is ${birthday.name}'s birthday. ${birthday.greeting}`
        b_list.appendChild(el)
    });
  });

})

