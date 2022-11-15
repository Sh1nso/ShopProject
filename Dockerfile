FROM python:3.10
WORKDIR /DimaTechTEST
RUN git clone https://github.com/Sh1nso/ShopProject
RUN pip install -r ./ShopProject/requirements.txt
COPY ./wait-for-it.sh /DimaTechTEST/ShopProject/wait-for-it.sh
CMD [ "python3", "./ShopProject/app.py"]