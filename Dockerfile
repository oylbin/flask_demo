FROM python:3.7-alpine
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install -i https://pypi.tuna.tsinghua.edu.cn/simple -r requirements.txt
COPY . .
ENV FLASK_ENV=production
ENV FLASK_APP=flask_demo
#ENV FLASK_DEMO_SETTINGS_FILE=/path/to/production_settings.py
CMD ["python", "-m", "flask", "run", "-h", "0.0.0.0", "-p", "80"]