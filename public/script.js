<script>
    const slider = documnet.getElementById('rangeValue');
    const submitButton = document.getElementById('submit');
    const output = document.getElementById('Prediction');

    function prediction() {
        output.innerHTML = '';
    }

    submitButton.adddEventListener('click', prediction);
</script>