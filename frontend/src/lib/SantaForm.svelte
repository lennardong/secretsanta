<script>
    let participants = [];

    function addParticipant() {
        const newParticipantName = `Participant ${participants.length + 1}`;
        participants.push(newParticipantName);
    }

    function toggleParticipant(row, col) {
        // Toggle the state of the checkbox
        participants[row][col] = !participants[row][col];
    }

    $: matrix = participants.map((_, rowIndex) => {
        return participants.map((_, colIndex) => {
            if (rowIndex === colIndex) return null; // A participant cannot be paired with themselves
            return {
                row: rowIndex,
                col: colIndex,
                checked: true // Initially, all names are checked against all other names
            };
        });
    });
</script>

<style>
    .matrix-form {
        display: grid;
    }
    .cell {
        padding: 0.5rem;
        text-align: center;
    }
</style>

<button on:click={addParticipant}>Add Participant</button>

<div class="matrix-form">
    {#each matrix as row, rowIndex}
        <div class="row">
            {#each row as cell, colIndex}
                {#if cell !== null}
                    <div class="cell">
                        <input
                            type="checkbox"
                            bind:checked={cell.checked}
                            on:click={() => toggleParticipant(cell.row, cell.col)}
                        />
                        <label>
                            {participants[cell.row]} &lt;-&gt; {participants[cell.col]}
                        </label>
                    </div>
                {/if}
            {/each}
        </div>
    {/each}
</div>
