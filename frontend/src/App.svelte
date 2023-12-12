<script>
  import svelteLogo from './assets/svelte.svg';
  import viteLogo from '/vite.svg';
  import Counter from './lib/Counter.svelte';
  import About from './lib/About.svelte';
  import InputForm from './lib/InputForm.svelte';
  import OutputPairs from './lib/OutputPairs.svelte';
</script>


<main>
  <div class = "frame">

    <div class="container">
      <div class="sub-container" id="A1">
        <About />
      </div>
      <div class="sub-container" id="A2">
        <InputForm />
      </div>
      <div class="sub-container" id="A3">
        <OutputPairs />
      </div>
    </div>

    <footer class="footer" id="B">
      <p>built by lennardong | Github Repo</p>
    </footer>
  </div>
</main>

<style>
  .frame {
    display: flex;
    flex-direction: column;
    height: 90vh;
    width: 90vw;
    border: 1px solid black;
    box-sizing: border-box;
    text-align: left;
  }

  .container {
    display: flex;
    flex: 1; /* Take the remaining height */
    background: #fff; /* Background color for A */
    border-bottom: 1px solid black;
  }

  .sub-container {
    flex-direction: column;
    flex: 1; /* Distribute space equally */
    display: flex;
    justify-content: left; /* Center content horizontally */
    align-items: baseline;
    border-right: 1px solid black; /* Add right border */
    padding: 2rem;
  }

  /* Remove the right border for the last sub-container */
  .sub-container:last-child {
    border-right: none;
  }

  .footer {
    height: auto; /* Auto height based on content */
    padding: 0.5rem; /* Padding for some space */
    padding-right: 2rem;
    text-align: right; /* Center text */
    background: white; /* Background color for B */
  }
</style>
