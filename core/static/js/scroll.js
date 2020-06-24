const menuItens = document.querySelectorAll('a')

menuItens.forEach(item => {
    item.addEventListener('click', scrollTo)
})

function scrollTo(event) {
    event.preventDefault()
    const element = event.target

    const id = element.getAttribute('href')
    const section = document.querySelector(id).offsetTop


    window.scroll({
        top: section,
        behavior: "smooth"
    })
}