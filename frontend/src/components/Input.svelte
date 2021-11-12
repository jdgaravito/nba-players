<script>
	export let id;
	export let label;
	export let value;
	export let placeholder = '';
	export let type = 'text';
	export let helptext = '';
	export let optional = null;
	export let valid = true;
	export let validityMessage = '';
	let touched = false;

</script>

<div class="formControl">
	<div class="label-container">
		<img src="../../static/height.svg" alt="icon-label" />
		<label for={id}>
			{label}
			{#if optional}
				<span class="optionalField">(optional)</span>
			{/if}
		</label>
	</div>

	<p class="helperText">{helptext}</p>
	<input
		class:invalid={!valid && touched}
		{type}
		{id}
		{value}
		{placeholder}
		on:input
		on:blur={() => (touched = true)}
		required
		min="10"
		max="200"
	/>
	{#if validityMessage && !valid && touched}
		<p class="error-message">
			{validityMessage}
		</p>
	{/if}
</div>

<style>
	:global(.invalid) {
		border-color: red;
	}
	input {
		display: block;
		width: 100%;
		font: inherit;
		border: none;
		border-radius: 3px;
		padding: 0.7rem 0.6rem 0.7rem 0.6rem;
		background: var(--input-color);
	}

	input:hover {
		background: #7556a3;
		border-color: #ffffff;
	}
	input::placeholder {
		font-weight: 300;
		color: #fff6f8;
		opacity: 50%;
	}
	input:focus {
		border-color: #ffffff;
		border: 1px solid #ffffff;
		outline: none;
		color: #ffffff;
		transition: border-color 0.1s ease-out;
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
	}
	img {
		width: 1.3rem;
		padding-right: 0.5rem;
	}
	.optionalField {
		font-weight: 100;
		opacity: 50%;
		display: inline-block;
	}
	.helperText {
		color: #fff6f8;
		font-weight: 300;
		opacity: 80%;
		margin: 0.5rem 0 0.5rem 0;
	}
	.formControl {
		padding: 0.5rem 0;
		width: 100%;
		margin: 0.25rem 0;
	}
	.invalid {
		border-color: #ef798a;
		background: #fff6f8;
	}
	.error-message {
		color: #ef798a;
		font-weight: 100;
	}
</style>
