import './App.css';
import Menu from './components/Menu';
import Home from './components/Home';
import Products1 from './components/Products1';
import Products2 from './components/Products2';
import Footer from './components/Footer';
import SideMenu from './components/SideMenu';


function App() {
  return (
    <div className="App">
      <Menu />
      <SideMenu />
      <div id='content'>
        <Home />
        <Products1 />
        <Products2 />
      </div>
      <Footer />
    </div>
  );
}

export default App;
