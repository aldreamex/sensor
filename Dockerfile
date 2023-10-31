FROM python:3.11

RUN mkdir -p /home/app


# Install pip requirements
RUN python -m pip install --upgrade pip

RUN pip install gunicorn

COPY ./requirements.txt .
RUN pip install -r requirements.txt


RUN groupadd app
RUN useradd -m -g app app -p dfqw12fewefwq
RUN usermod -aG app app

ENV HOME=/home/app
ENV APP_HOME=/home/app/sensor

RUN mkdir $APP_HOME
RUN mkdir $APP_HOME/static
RUN mkdir -m 777 $APP_HOME/media
WORKDIR $APP_HOME


COPY . $APP_HOME

RUN chown -R app $APP_HOME

USER app