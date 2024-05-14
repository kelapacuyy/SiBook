import React, { Component } from "react";
import Slider from "react-slick";
import '../style/slick.css';
import '../style/slick-theme.css';
import news from "../data/news";


export default class SimpleSlider extends Component {
  render() {
    const settings = {
      autoplay: true,
      autoplaySpeed: 3000,
      dots: false,
      infinite: true,
      speed: 500,
      slidesToShow: 1,
      slidesToScroll: 1
    };

    return (
      <div id="news-slider">
        <Slider {...settings}>
          {
            news.map((slide) => (
              <img src={slide.image}></img>
            ))
          }
        </Slider>
      </div>
    )
  }
}