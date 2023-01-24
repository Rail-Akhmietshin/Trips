let modal = document.getElementById("myModal");
let btn = document.getElementById("myBtn");
let shut = document.getElementsByClassName("shut")[0];

btn.onclick = function () {
    modal.style.display = "block";
}

shut.onclick = function () {
    modal.style.display = "none";
}

window.onclick = function(event) {
    if (event.target == modal) {
        modal.style.display = "none";
    }
}



// const popupLinks = document.querySelectorAll(".popup-link");
// const body = document.querySelectorAll("body");
// const lockPadding = document.querySelectorAll(".lock-padding");

// let unlock = true;  /* Чтобы не было двойных кликов*/

// const timeout = 800     /* Должно совпадать со свойством transition (0.8) */

// if (popupLinks.length > 0) {
//     for (let index = 0; index < popupLinks.length; index++) {
//         const popupLink = popupLinks[index];
//         popupLink.addEventListener("click", function (e) {  /* Навешиваем событие click */
//             const popupName = popupLink.getAttribute('href').replace('#', '');  
//             const curentPopup = document.getElementById(popupName);
//             popupOpen(curentPopup);
//             e.preventDefault();     /* запрещаем обновлять страницу */
//         });
//     }
// }

// const popupCloseIcon = document.querySelectorAll(".close-popup");

// if (popupCloseIcon.length > 0) {
//     for (let index = 0; index < popupCloseIcon.length; index++) {
//         const el = popupCloseIcon[index];
//         el.addEventListener('click', function (e) {
//             popupClose(el.closest('.popup'));
//             e.preventDefault();
//         })
//     }
// }

// function popupOpen(curentPopup) {
//     if (curentPopup && unlock) {
//         const popupActive = document.querySelector('.popup.open');
//         if (popupActive) {
//             popupClose(popupActive, false);
//         } else {
//             bodyLock();
//         }

//         curentPopup.classList.add('open');
//         curentPopup.addEventListener('click', function (e) {
//             if (!e.target.closest('.popup__content')) {
//                 popupClose(e.target.closest('.popup'));
//             }
//         })
//     }
// }