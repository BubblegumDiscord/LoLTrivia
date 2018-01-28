FROM python:3.6-slim-jessie
RUN apt-get update
RUN apt-get install -y gcc
RUN apt-get install -y libffi-dev libssl-dev zlib1g-dev
 
RUN pip install discord.py html2text fuzzywuzzy requests
RUN pip install pyjwt

ADD . /

CMD [ "python", "./run.py" ]
