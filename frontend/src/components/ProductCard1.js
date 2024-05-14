import '../style/Products1.css';

function ProductCard({product}) {
  return (
    <div className="product-card">
      <img className="product-image" src={product.image}></img>
      <div className="product-info">
        <p className="product-title">{product.title}</p>
        <p className="product-author">{product.author}</p>
        <p className="product-price">{`$${product.price}`}</p>
        
        <div className='cart-div'>
          <div className="cart-button button">
            <img className='cart-icon' src='images/icons/icons8-cart-white-30.png'></img>
            <p>Masukkan ke Keranjang</p>
          </div>
        </div>
      </div>
    </div>
  )
}

export default ProductCard