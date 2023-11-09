#!/urs/bin/node
// Import the axios module
const axios = require('axios');

// Function to get and print characters for a given movie ID
async function getCharacters(movieId) {
  try {
    // Star Wars API base URL
    const baseUrl = 'https://swapi.dev/api/films/';

    // Make a request to the Star Wars API for the specified movie
    const response = await axios.get(`${baseUrl}${movieId}/`);

    // Extract the characters list from the API response
    const charactersUrls = response.data.characters;

    // Use Promise.all to fetch character details concurrently
    const charactersPromises = charactersUrls.map(async (characterUrl) => {
      const characterResponse = await axios.get(characterUrl);
      return characterResponse.data.name;
    });

    // Wait for all character details to be fetched
    const characters = await Promise.all(charactersPromises);

    // Print each character's name
    characters.forEach((character) => {
      console.log(character);
    });
  } catch (error) {
    console.error(`Error: ${error.message}`);
  }
}

// Check if the correct number of command line arguments is provided
if (process.argv.length !== 3) {
  console.log('Usage: node 0-starwars_characters.js <movie_id>');
  process.exit(1);
}

// Get the movie ID from the command line arguments
const movieId = process.argv[2];

// Call the function to get and print characters
getCharacters(movieId);


