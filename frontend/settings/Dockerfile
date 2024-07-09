# Use the official Node.js image as the build stage
FROM node:16-alpine as build-stage

# Set the working directory
WORKDIR /app

# Copy the package.json and yarn.lock files
COPY package.json yarn.lock ./

# Install the dependencies
RUN yarn install

# Copy the rest of the application code
COPY . .

# Build the application
RUN yarn build

# Use the official Nginx image as the production stage
FROM nginx:stable-alpine as production-stage

# Copy the built application from the build stage
COPY --from=build-stage /app/dist /usr/share/nginx/html

# Expose the port Nginx will serve on
EXPOSE 80

# Define the default command to run Nginx
CMD ["nginx", "-g", "daemon off;"]
