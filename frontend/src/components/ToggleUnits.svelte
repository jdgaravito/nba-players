<script>
	import { createEventDispatcher } from 'svelte';
	const dispatch = createEventDispatcher();
	export let value = true;
	export let label;
	let active = true;
	
	
	function handleClick(){
		active = !active;
		value = !value;
		dispatch(
			'message', value
		)
	}

</script>

<div class="formControl">
	<div class="label-container">
		<img src="../../static/units.svg" alt="icon-label" />
		<label for="radio1">
			{label}
		</label>
	</div>
	<p class="helper-text">Please select the units</p>
	<div class="buttons-wrapper">
		<div class="button-container">
			<input type="radio" class="radio_item" bind:value={value} name="item" id="radio1" />
			<label class="label_item" for="radio1">
				<button class:active={active} type="button" on:click={handleClick}> Inches </button>
			</label>
		</div>
		<div class="button-container">
			<input type="radio" class="radio_item" bind:value={value} name="item" id="radio2" />
			<label class="label_item" for="radio1">
				<button class:active={!active} type="button" on:click={handleClick}> Meters </button>
			</label>
		</div>
	</div>
</div>


<style>
	.radio_item {
		display: none !important;
	}

	.label_item {
		opacity: 100;
	}

	.radio_item:checked + label {
		opacity: 1;
	}

	label {
		display: block;
		margin-bottom: 0.1rem;
		width: 100%;
		font-weight: bold;
		color: #fff6f8;
	}
	.label-container {
		display: flex;
        padding-top: 1rem;
	}
	img {
		width: 1.3rem;
		padding-right: 0.5rem;
	}

	p{
		color: #ffffff;
		padding-top: 1rem;
		font-weight: 300;
		opacity: 80%;
	}
	.buttons-wrapper {
		display: flex;
        padding: 1rem 0 3rem 0;
	}

    button {
		border: 2px solid var(--input-color);
        font: inherit;
        font-size: 1rem;
        margin-right: 1.1rem;
        padding: 0.5rem 1rem 0.5rem 1rem;
		color: #ffffff;
		background: var(--input-color);
		border-radius: 5px;
		cursor: pointer;
    }
	button:hover{
		border-color: #ffffff;

	}

	.active{
		color: var(--primary-color);
		background: #ffffff;

	}	


</style>
