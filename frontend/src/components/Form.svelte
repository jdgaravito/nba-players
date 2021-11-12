<script>
	
	import Input from './Input.svelte';
	import ToggleUnits from './ToggleUnits.svelte';

	let units = 'in';
	let heightSum = "";
	let heightMessage = '';
	let toggleValue = true;

	//Format values
	if (units == 'in') {
		heightMessage = 'Maximum height is 200in';
	} else {
		heightMessage = 'Maximum height is 4.6m';
	}

	if (toggleValue){
		units = 'in';
	}
	else{
		units = 'meters'
	}

	//Submitting the form
	const submit = ({target: form}) => {
		const values = {heightSum, units}
		console.log(values)
	}

</script>

<div class="formWrapper">
	<form on:submit|preventDefault={submit}>
		<Input
			type="number"
			id="height-input"
			label="Player's Height Sum"
			value={heightSum}
			placeholder={heightMessage}
			helptext="Please write the sum of heights for a pair of players"
		/>
		<ToggleUnits label="Units:" value={toggleValue} />

		<button class="submit" type="submit">Submit</button>
	</form>
</div>

<style>
	.submit{
		border: 2px solid #ffffff;
        font: inherit;
        font-size: 1rem;
        margin-right: 1.1rem;
        padding: 0.5rem 5rem 0.5rem 5rem;
		color: #ffffff;
		background: #ffffff;
		border-radius: 5px;
		cursor: pointer;
		color: var(--primary-color);
		font-weight: 700;
	}
	.submit:hover, 
	.submit:active{
		background: var(--scroll-color);
		color: #ffffff;
		transform: translateY(-1px);
		transition: transform 0.2s ease-in-out;	
	}
</style>
