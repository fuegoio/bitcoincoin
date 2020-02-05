FROM node:10.16.0-alpine as build-stage
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

FROM nginx:1.15

COPY --from=build-stage /app/dist/ /usr/share/nginx/html