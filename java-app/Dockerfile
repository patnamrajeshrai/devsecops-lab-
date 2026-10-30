FROM eclipse-temurin:17-jre-alpine

WORKDIR /app

RUN apk add --no-cache procps \
    && addgroup -S appgroup \
    && adduser -S appuser -G appgroup

COPY --chown=appuser:appgroup target/devsecops-demo-1.0.0.jar app.jar

USER appuser

HEALTHCHECK --interval=30s --timeout=5s --start-period=5s --retries=3 \
    CMD pgrep -f '[j]ava -jar app.jar' || exit 1

ENTRYPOINT ["java", "-jar", "app.jar"]
