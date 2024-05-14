import WishlistModal from './modals/WishlistModal';
import { openTwitter, openIG, openLK } from '../helpers';
import '../style/Products1.css';
import CartModal from './modals/CartModal';
import RegisterModal from './modals/RegisterModal';
import '../style/Menuafterlogin.css';
import { useState } from 'react';


function Menu() {
  const [openWishlist, setOpenWishlist] = useState(false)
  const [openRegister, setOpenRegister] = useState(false)
  const [openCart, setOpenCart] = useState(false)

  function handleSideMenuVisibility() {
    let sideMenu = document.getElementById("side-menu")
    if(sideMenu.className === "side-menu-closed") {
      sideMenu.className = "side-menu-opened"
    } else {
      sideMenu.className = "side-menu-closed"
    }
  }

  return (
    <div>
      <div id='page-header'>
        <p>Follow us: </p>
        <div id='menu-div2'>
          <img className='icon-menu-item' src='images/icons/icons8-heart-50.png' onClick={() => {openTwitter() }}></img>
          <img className='icon-menu-item' src='images/icons/icons8-heart-50.png' onClick={() => {openIG() }}></img>
          <img className='icon-menu-item' src='images/icons/icons8-heart-50.png' onClick={() => {openLK() }}></img>
        </div>
        <div id='user-div'>
          <p className='icon-menu-item' onClick={() => { setOpenWishlist(true) }}>Butuh Bantuan?</p>
        </div>      
      </div> 

      <div id='menu-div'>
        <div id='menu-items-div'>
          <a className='menu-item' href='#home-page'>Home</a>
          <a className='menu-item' href='#about-page'>About</a>
          <a className='menu-item' href='#products-page'>Products</a>
          <a className='menu-item' href="#review-page">Review</a>
          <a className='menu-item' href='#contact-page'>Contact</a>
        </div>
        <div id='search-div'>
          <img src='images/icons/icons8-search-30.png'></img>
          <input type='text' placeholder='Search website...' id='search-input'></input>
        </div>
        <div className="cart-button1 button">
          <img className='cart-icon1' src='images/icons/icons8-cart-white-30.png' onClick={() => setOpenCart(true)}></img>
          <img className='cart-icon1' src='images/icons/icons8-cart-white-30.png' onClick={() => setOpenWishlist(true)}></img>
        </div>
        <div class="button-grid1">
          <button class="button11">user16784</button> {/* ini nanti tinggal diganti dengan user2ny*/}
        </div>
        <div>
          <img id='hamburger-menu-icon' src='images/icons/icons8-hamburger-menu-50.png' onClick={() => { handleSideMenuVisibility() }}></img>
        </div>
      </div>    
      { openWishlist && <WishlistModal setOpenWishlistModal={setOpenWishlist}/> }
      { openCart && <CartModal setOpenCartModal={setOpenCart}/> }
    </div>
  ); 
}

export default Menu;