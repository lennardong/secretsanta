/*
  This file contains the logic for parsing the input from the form and calling the API.
  It takes in input as a full string then formats it to a dictionary of participants and their exclusions.
  The API call is made to the backend.
*/

// const BASE_URL = 'http://127.0.0.1:8000';
const BASE_URL = '/api';

async function callApi(data) {
  const response = await fetch(`${BASE_URL}/secret-santa-stack/`, {
      method: 'POST',
      headers: {'Content-Type': 'application/json'},
      body: JSON.stringify({ names: data }),
      // mode: 'no-cors', 
      // TODO - remove no-cors mode
  });

  if (!response.ok) {
      throw new Error(`API call failed with status ${response.status}: ${await response.text()}`);
  }
  return response.json();
}


async function parseParticipants(formInput) {
  console.log('Parsing Participants', formInput);
  let participant2exclusions = {};

  let lines = formInput.split('\n').map(line => line.trim());
  let group = [];
  console.log('lines', lines);

  for (let line of lines) {
    if (line.trim().length > 0 && line[0] !== '#') {
      let parts = line.split('(');
      let name = parts[0].trim();
      
      group.push(name);

      // Check for exclusions (i.e. items after `(`)
      if (parts.length > 1) {
        let exclusions = parts[1].split(')')[0].split(',').map(item => item.trim());
        participant2exclusions[name] = exclusions;
      } else {
        participant2exclusions[name] = [];
      }
    }

    if (line.trim().startsWith('#')) {
      group.forEach(member => {
        if (!participant2exclusions[member]) {
          participant2exclusions[member] = group.filter(g => g !== member);
        } else {
          participant2exclusions[member] = [...new Set([...participant2exclusions[member], ...group.filter(g => g !== member)])];
        }
      });
      group = [];
    }
  }

  if (group.length > 0) {
    group.forEach(member => {
      if (!participant2exclusions[member]) {
        participant2exclusions[member] = group.filter(g => g !== member);
      } else {
        participant2exclusions[member] = [...new Set([...participant2exclusions[member], ...group.filter(g => g !== member)])];
      }
    });
  }

  console.log('API input:', participant2exclusions);
  let result = await callApi(participant2exclusions);
  console.log('API output:', result);
  return result;
}
  
export { parseParticipants };