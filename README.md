<h2 style="display: inline-block">Table of Contents</h2>
<ol>
    <li><a href="#about-the-project">About Real Estate Machine Learning project</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
</ol>

## About Real Estate Machine Learning project

I wanted to experiment Machine Learning and Python/Flask a little bit, so I came up with this toy project.

I've started from a sci-kit model that I created from the Melbourne Housing Market dataset on Kaggle (https://www.kaggle.com/anthonypino/melbourne-housing-market).

By the way, you can find the Github repository with the Jupiter Notebook I created for the afore mentioned model at https://github.com/nicola-piccolo/real-estate-machine-learning-model .

I have then built a simple REST API Flask application server that predicts a Melbourne property price by using a few parameters.

The application supports also an endpoint to store and retrieve records related to property from a MySQL instance.

Last but not least, I also played around with Docker and this whole project can also be run in a network of Docker containers.

### Built With

* Python 3.6
* Flask 1.1
* Gunicorn 20.0
* Mysql 8
* Docker 20.10
* Nginx 1.19

## License

Copyright (c) 2021 Nicola Piccolo

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.

## Contact

Nicola Piccolo - https://www.linkedin.com/in/nicola-piccolo-b939523/