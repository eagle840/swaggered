# swaggered
swagger code gen

1. head over to editor.swagger.io and generate your swagger code for python-flask
2. select server code gen on that page - it will download a folder.
3. paste the folder into a new repo (ie this one)
4. clone it to pc and work file

 * note, change the swagger codegen requirements.txt to show
connexion == 1.1.15  <= change to **2.6.0**
python_dateutil == 2.6.0
setuptools >= 21.0.0

* note:  a component is missing, (since v2) run: pip3 install connexion[swagger-ui]
         problem with pip3
         run:
         apt remove python3-pip
         apt install python3-pip
