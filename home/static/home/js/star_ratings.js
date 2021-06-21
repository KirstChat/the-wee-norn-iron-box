const starRating = document.querySelectorAll('.star-rating');

starRating.forEach(rating => {
    if (rating.innerText === "5") {
        rating.innerHTML = `
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>`
    } else if (rating.innerText === "4") {
        rating.innerHTML = `
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>`
    } else if (rating.innerText === "3") {
        rating.innerHTML = `
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>`
    } else if (rating.innerText === "2") {
        rating.innerHTML = `
                    <i class="fas fa-star"></i>
                    <i class="fas fa-star"></i>`
    } else {
        rating.innerHTML = `<i class="fas fa-star"></i>`
    };
});