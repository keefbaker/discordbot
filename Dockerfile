FROM python
COPY main.py main.py
RUN pip install discord.py && chmod 755 main.py && useradd richard
USER richard
ENTRYPOINT ["./main.py"]
