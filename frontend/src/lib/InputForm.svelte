<script>
  let count = 0
  const increment = () => {
    count += 1
    }
</script>

<!-- ############################################ -->
<!-- # CONTENT -->
<!-- ############################################ -->

<b>
  Lets make your SecretSanta pool
</b>

<ul>
  <li><b>Group Exclusions</b> - Define new groups with a # header. Every person inside is comma seperated. People in the same group will not be matched. </li>
  <li><b>Special Exclusions</b> -  Define special exclusions with a () postfix to a name. People in () after a name will also be excluded from matching. </li>
</ul>

<input type='text' class='my-text-box' value="Default text" />


<button> Generate Pairings</button>


<!-- ############################################ -->
<!-- # STYLES -->
<!-- ############################################ -->

<style>

  li{
    font-size: small;
  }

  .my-text-box {
    font-size: 10px; /* or larger */
    height: 20em; /* or larger */
    width: 100%; /* or larger */
    height: 100%;
    border-radius: 0.5rem;
    border: 1px solid white;
    background-color: lightgray;
  }

</style>