<!-- ############################################ -->
<!-- # LOGIC JS -->
<!-- ############################################ -->

<script>
  export let pairings;

  let formattedPairings = '';

  // Format pairings whenever the `pairings` prop changes
  $: if (pairings) {
    formattedPairings = pairings.map(([gifter, giftee]) => 
      `${gifter} -> ${giftee}`).join('\n');
  }
</script>



<!-- ############################################ -->
<!-- # CONTENT HTML -->
<!-- ############################################ -->

<b>Pairings</b>
<div class="output-container">
  <textarea bind:value={formattedPairings} readonly></textarea>
</div>

<!-- ############################################ -->
<!-- # STYLES CSS -->
<!-- ############################################ -->

<style>
  .output-container {
    display: flex;
    flex-direction: column;
    align-items: center;
    height: 100%;
    width: 100%;
    box-sizing: border-box;
    padding: 5px;
  }
  b{
    margin-bottom: 1rem;
  }
  textarea {
    flex: 1;
    padding: 10px;
    line-height: 1em;
    border-radius: 0px;
    height: 100%;
    width: 100%;
    
    margin-bottom: 1rem;
    font-size: 10px;
    font-family: "Consolas", monospace;
    border: 1px solid rgb(0, 0, 0);
    color: black;
    background: rgb(255, 255, 255);
  }
</style>