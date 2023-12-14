const BASE_URL = 'http://localhost:5000';

async function callApi(data) {
    const response = await fetch(`${BASE_URL}/api/parseParticipants`, {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify(data),
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

  console.log(participant2exclusions);
  return participant2exclusions;
}

async function parseParticipants_v1(formInput) {
  console.log('Parsing Participants', formInput);
  // Hashmap of participants {name: [exclusions]}
  let participant2exclusions = {};

  // Process inputs
  let lines = formInput.split('\n').map(line => line.trim());
  console.log('lines', lines);
  let group = [];
  
  for (let line of lines) {

    // If line is not empty or does not start with #, then it is a participant
    if (line.length > 0 && line[0] !== '#'){
        
      // Check for name (up to first ()
      // Add to group array
      let name = line.split('(')[0].trim();
      group.push(name);
      
      // Get names in (), splitting each item inside by comma
      // if exclusions is not empty, then remove whitespace from beginning and end of each item
      let exclusions = line.split('(')[1].split(')')[0].split(',');
      if (exclusions.length > 0){
        exclusions = exclusions.map(item => item.trim());
      } else {
        exclusions = [];
      }

      
      // Add name to dictionary if not already there and add exclusions as values
      if (!participant2exclusions[name]){
        participant2exclusions[name] = exclusions;
      }
    }
    
      // if line starts with #, then all items before the line are a group. 
    if (line[0] === '#'){
      for (let member of group){
        // find dictionary entry for member and all entire group to exclusions
        if (!participant2exclusions[member]){
          participant2exclusions[member] = group;
        } else {
          // append group to existing exclusions
          participant2exclusions[member] = participant2exclusions[member].concat(group);
        }
      }
      // reset group
      group = []; 
    }
  }

  // Final Check
  // if there are remaining items in group, do the same as above
  if (group.length > 0){
    for (let member of group){
      if (!participant2exclusions[member]){
        participant2exclusions[member] = group;
      } else {
        participant2exclusions[member] = participant2exclusions[member].concat(group);
      }
    }
  }

  console.log(participant2exclusions);
  // TODO implement call to backend
  return participant2exclusions;

}
  
export { parseParticipants };
