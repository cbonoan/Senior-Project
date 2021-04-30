const date = new Date();
date.setDate(1);
const renderCalendar = () => {
const monthDays = document.querySelector('.days');
const lastDay = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDate();
const firstDayIndex = date.getDay();
const prevLastDay = new Date(date.getFullYear(), date.getMonth(), 0).getDate();
const lastDayIndex = new Date(date.getFullYear(), date.getMonth() + 1, 0).getDay();
const nextDays = 7 - lastDayIndex - 1;

    const month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ];
    document.querySelector('.date h1').innerHTML = month[date.getMonth()];
    document.querySelector('.date p').innerHTML = new Date().toDateString();
    
    let days = "";
    for(let x = firstDayIndex; x > 0; x--)
    {
       days += '<div class = "prev-date">'+(prevLastDay - x + 1)+'</div>'; 
       
    }
    for(let i = 1; i <= lastDay; i++)
    {
        days += '<div>'+i+'</div>';
        monthDays.innerHTML = days;
    }
    for(let j = 1; j<=nextDays; j++)
    {
        days += '<div class = "next-date">'+j+'</div>';
        monthDays.innerHTML = days;
    }

}
console.log('{{ feeling }}');

document.querySelector('.prev').
addEventListener('click',()=> {
    date.setMonth(date.getMonth()-1);
    renderCalendar();
})

document.querySelector('.next').
addEventListener('click',()=> {
    date.setMonth(date.getMonth()+1);
    renderCalendar();
})
renderCalendar();



