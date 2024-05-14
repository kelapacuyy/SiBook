import '../style/Footer.css';
import { openTwitter, openIG, openLK } from '../helpers';

function Footer() {
  
  return (
    <div id="footer-line">
    <div id="footer">
      <div id="footer-info">
        <div id="footer-contact">
          <div id="footer-title">
            <p>Ikuti Kami</p>
          </div>
          <div className='footer-contact-link'>
            <img src='images/icons/icons8-location-white-50.png'></img>
            <p onClick={() => {openTwitter() }}>SiBook on Twitter</p>
          </div>
          <div className='footer-contact-link'>
            <img src='images/icons/icons8-phone-white-50.png'></img>
            <p onClick={() => {openIG() }}>SiBook on Instagram</p>
          </div>
          <div className='footer-contact-link'>
            <img src='images/icons/icons8-mail-white-50.png'></img>
            <p onClick={() => {openLK() }}>SiBook on Linkedin</p>
          </div>
        </div>

        <div id="footer-contact">
          <div id="footer-title">
            <p>Jelajahi SiBook</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openTwitter() }}>Tentang Kami</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openIG() }}>Karir</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Kerjasama</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Dashboard</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Keamanan</p>
          </div>
        </div>

        <div id="footer-contact">
          <div id="footer-title">
            <p>Layanan Pelanggan</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openTwitter() }}>Syarat dan Ketentuan</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openIG() }}>Syarat Pengaduan</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Prosedur Pengembalian</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Kebijakan Privasi</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Forums</p>
          </div>
        </div>

        <div id="footer-contact">
          <div id="footer-title">
            <p>Akses Cepat</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openTwitter() }}>Hubungi Kami</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openIG() }}>Blog</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Pengembalian Barang</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>Lacak Pesanan Pembeli</p>
          </div>
          <div className='footer-contact-link'>
            <p onClick={() => {openLK() }}>FAQ</p>
          </div>
        </div>

      </div>
      <p id="copyright">----------------- © SiBook 2024. Hak Cipta Dilindungi -----------------</p>    
    </div>
    </div>
  )
}

export default Footer;