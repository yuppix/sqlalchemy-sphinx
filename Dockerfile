FROM python:2.7
ADD ./ /cc-sphinx-alchemy/
WORKDIR /cc-sphinx-alchemy
COPY docker_entrypoint.sh /
ENTRYPOINT ["/docker_entrypoint.sh"]
CMD ["test27"]
