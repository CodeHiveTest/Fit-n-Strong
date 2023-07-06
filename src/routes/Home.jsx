import "./../styles/Home.css";
import { UncontrolledCarousel } from "reactstrap";
import slider1 from "./../assets/images/slider1.png";
import slider2 from "./../assets/images/slider2.png";
import slider3 from "./../assets/images/slider3.png";

export default function Home() {
    return (
        <div className="container">
            <h2 className="title">Bienvenido, Usuario a <br/>Fit and Strong</h2>
            <div className="slider-container">
                <UncontrolledCarousel
                items={[
                    {
                    altText: 'Slide 1',
                    caption: 'Slide 1',
                    key: 1,
                    src: slider1
                    },
                    {
                    altText: 'Slide 2',
                    caption: 'Slide 2',
                    key: 2,
                    src: slider2
                    },
                    {
                    altText: 'Slide 3',
                    caption: 'Slide 3',
                    key: 3,
                    src: slider3
                    }
                ]}
                />
            </div>
        </div>
    );
}