export function openTwitter() {
  window.open("https://twitter.com/");
}

export function openIG() {
  window.open("https://instagram.com/");
}

export function openLK() {
  window.open("https://linkedin.com/");
}

export function calculateCartTotal(cart) {
  let totalPrice = 0
  cart.forEach(item => {
    totalPrice += parseFloat(item.price)
  })
  return totalPrice
}

export function getRatingStars(rating) {
  console.log(rating)
  rating = parseInt(rating)
  let stars = []
  for(let i = 0; i < 5; i++) {
    stars.push('images/icons/icons8-star-gold-outline.png')
  }
  for(let i = 0; i < rating; i++) {
    stars[i] ='images/icons/icons8-star-gold.png'
  }
  return stars
}