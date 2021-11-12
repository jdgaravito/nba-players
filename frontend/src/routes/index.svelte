<script>
	import Nav from '../components/Nav.svelte';
	import Form from '../components/Form.svelte';
</script>

{#if false}<slot />{/if}
<div class="wrapper">
	<div class="inner">
		<Nav />
		<main>
			<section class="form-container">
				<Form />
			</section>
			<section class="image-container">
				<img src="../../static/player.png" alt="" />
			</section>
			<section class="pairs-container" />
		</main>
	</div>
</div>

<style>
	main {
		display: grid;
		grid-template-columns: 1fr 1fr 1.5fr;
		height: 85vh;
	}

	.form-container {
		padding: 3rem;
	}
</style>
