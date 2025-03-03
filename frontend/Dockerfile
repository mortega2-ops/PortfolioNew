# For production:
# - Use a multi-stage build to create a smaller production image
# - Build static files and serve them with nginx
# - Remove development-specific configurations

# Development image (current setup)
FROM node:18-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the code
COPY . .

# Expose the port
EXPOSE 5173

# Start the application in development mode
CMD ["npm", "run", "dev", "--", "--host", "0.0.0.0"]

# PROD: For production, replace the above with a multi-stage build like:
# 
# # Build stage
# FROM node:18-alpine AS build
# 
# WORKDIR /app
# 
# COPY package*.json ./
# RUN npm ci
# 
# COPY . .
# RUN npm run build
# 
# # Production stage
# FROM nginx:alpine
# 
# # Copy built assets from build stage
# COPY --from=build /app/build /usr/share/nginx/html
# 
# # Copy nginx configuration if needed
# # COPY ./nginx/default.conf /etc/nginx/conf.d/default.conf
# 
# EXPOSE 80
# 
# CMD ["nginx", "-g", "daemon off;"] 