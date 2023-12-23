<!-- ############################################ -->
<!-- # LOGIC (JS)-->
<!-- ############################################ -->

<script>
  // Import components
  import About from './lib/About.svelte';
  import InputForm from './lib/InputForm.svelte';
  import OutputPairs from './lib/OutputPairs.svelte';

  // create a variable and assign output to it
  let outputData = '...waiting for inputs';
  function handleUpdate(event){
    outputData = event.detail; 
  }

</script>

<!-- ############################################ -->
<!-- # CONTENT (HTML) -->
<!-- ############################################ -->

<main>
  <div id = "frame">

    <!-- BODY -->

    <div id = "container" >
      <div id="sub-container">
        <About />
      </div>
      <div id="sub-container">
        <InputForm on:update={handleUpdate} />
      </div>
      <div id="sub-container">
        <OutputPairs pairings = {outputData}/>
      </div>
    </div>

    <!-- FOOTER -->

    <footer id="footer" class="footer">
      <p>built by lennardong | <a href = "https://github.com/lennardong/secretsanta">Github Repo </a></p>
    </footer>

  </div>
</main>

<!-- ############################################ -->
<!-- # STYLES (CSS) -->
<!-- ############################################ -->

<style>
  #frame {
    display: flex;
    flex-direction: column;
    height: 90vh;
    width: 90vw;
    border: 1px solid black;
    box-sizing: border-box;
    text-align: left;
  }

  #container {
    display: flex;
    flex-direction: row;
    flex: 1;  
    
  }

  #sub-container {
    flex-direction: column;
    flex: 1; /* Distribute space equally */
    display: flex;
    justify-content: left; /* Center content horizontally */
    align-items: baseline;
    border-right: 1px solid black;
    border-bottom: 1px solid black;
    padding: 2em;
  }

  #sub-container:last-child {
    border-right: none;
  }

  #footer {
    height: auto; /* Auto height based on content */
    padding: 0.5rem; /* Padding for some space */
    padding-right: 2rem;
    text-align: right;
    font-size: smaller;
  }

  .footer{
    text-align: right;
  }
</style>
