const covidNoticeBtn = document.querySelector('#collapse-btn')
const covidParagraph = document.querySelector('.covid-notice')
covidNoticeBtn.addEventListener('click', function(){
covidParagraph.classList.toggle('open')
})

