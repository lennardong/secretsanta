

<!-- ############################################ -->
<!-- # LOGIC -->
<!-- ############################################ -->

<script>
  // Input variable
  let input = `
# 
Larry (Gerald, MaryJ), Hannah, Mary, Jane 

# 
Gerald, MaryJ 

#
Anthony (Larry, Mary), Lucy, Kerry, Perry (Gerald, MaryJ)
`
  // Event trigger as callback function
  import { createEventDispatcher } from "svelte";
  const dispatch = createEventDispatcher();
  
  // Parse inputs and trigger callback
  function handleButtonClick(_input) {
    console.log(_input);
    let result = _input;
    dispatch('update', result)
  }

</script>

<!-- ############################################ -->
<!-- # CONTENT -->
<!-- ############################################ -->

<b>Lets make a participant pool!</b>
<ul>
  <li>
    <b>Group Exclusions</b> - Define new groups with a # header. Every person inside
    is comma seperated. People in the same group will not be matched.
  </li>
  <li>
    <b>Special Exclusions</b> - Define special exclusions with a () postfix to a
    name. People in () after a name will also be excluded from matching.
  </li>
</ul>


<div class="form-container">
  <textarea bind:value={input}></textarea>
  <button on:click={() => {handleButtonClick(input)}}>
    Generate Pairings
  </button>
</div>

<!-- ############################################ -->
<!-- # STYLES -->
<!-- ############################################ -->

<style>
  
  ul{
    margin-top: 1rem;
    font-size: small;
  }

  .form-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    padding: 5px;
  }

  h2 {
    margin-bottom: 0;
  }

  textarea {
    flex: 1;
    padding: 10px;
    line-height: 1em;
    border-radius: 5px;
    border: 1px solid black;
    height: 100%;
    width: 100%;

    margin-bottom: 1rem;
    font-size: 10px;
    font-family: "Consolas", monospace;
    color: greenyellow;
    background: black;
  }

  button {
    border: 1px solid black;
    border-radius: 50px;
    background: white;
    color: black;
    padding: 10px;
    font-size: small;
    font-weight: bold;
  }
</style>
