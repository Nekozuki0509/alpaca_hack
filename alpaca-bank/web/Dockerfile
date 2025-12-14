FROM node:25.2.1-slim
WORKDIR /app
COPY package.json package-lock.json /app/
RUN npm ci
COPY index.html app.js /app/
CMD ["node", "app.js"]