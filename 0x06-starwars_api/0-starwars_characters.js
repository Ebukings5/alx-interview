#!/usr/bin/node

const request = require('request');

// Ensure the user has provided the movie ID as a command-line argument
if (process.argv.length < 3) {
  console.error('Usage: ./0-starwars_characters.js <movie_id>');
  process.exit(1);
}

const movieId = process.argv[2];
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}/`;

// Function to fetch and print characters in order
function fetchCharacters(characters) {
  characters.forEach((characterUrl) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        console.error(error);
        return;
      }
      const character = JSON.parse(body);
      console.log(character.name);
    });
  });
}

// Fetch the movie data from the Star Wars API
request(url, (error, response, body) => {
  if (error) {
    console.error(error);
    return;
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  
  // Fetch and print character details
  fetchCharacters(characters);
});
