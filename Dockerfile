FROM python:3

# Server port and mongo port.
EXPOSE 5050
EXPOSE 27017

# Our project directory.
WORKDIR /usr/src/auth-py

COPY requirements.txt ./

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP="auth-py.py"
# Run the server.
CMD [ "python", "-m" , "flask", "run", "--host=0.0.0.0", "--port=5050"]

