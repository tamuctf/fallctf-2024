FROM bitnami/openldap:2.5.18

ARG port

ENV LDAP_ADMIN_USERNAME=admin \
    LDAP_ADMIN_PASSWORD=roMZCDMcFfKVhM5nUKyh8VrTf5anpDUt \
    LDAP_ROOT=dc=dap-me-up,dc=local \
    LDAP_USERS=bob \
    LDAP_PASSWORDS=QYwkvGAZ8iXymtZ9p0G187y77TRHrjNJ \
    LDAP_ADMIN_DN=cn=admin,dc=dap-me-up,dc=local

USER 0

RUN apt-get update && \
    apt-get install -y supervisor apache2 libapache2-mod-php php php-ldap

COPY index.php /var/www/html/index.php
COPY supervisord.conf /etc/supervisor/conf.d/supervisord.conf

RUN echo "ServerName localhost" >> /etc/apache2/apache2.conf && \
    sed -i "s/Listen 80/Listen ${port}/" /etc/apache2/ports.conf && \
    chown -R www-data:www-data /var/www/html && \
    rm /var/www/html/index.html

EXPOSE ${port}

CMD []
ENTRYPOINT ["/usr/bin/supervisord", "-c", "/etc/supervisor/conf.d/supervisord.conf"]
