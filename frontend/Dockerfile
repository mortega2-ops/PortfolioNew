FROM node:18-alpine as build

WORKDIR /app

# Copy package.json and package-lock.json
COPY package*.json ./

# Install dependencies
RUN npm ci

# Copy the rest of the code
COPY . .

# Build the application
RUN npm run build

# Production stage
FROM node:18-alpine

WORKDIR /app

# Copy built assets from the build stage
COPY --from=build /app/build ./build
COPY --from=build /app/package.json ./

# Install production dependencies
RUN npm ci --production

# Expose the port
EXPOSE 3000

# Start the application
CMD ["node", "build"] 