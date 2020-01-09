FROM python:2
ADD constantes.py /
ADD grid.py /
ADD main.py /
ADD posicao.py /
CMD [ "python", "./main.py" ]
