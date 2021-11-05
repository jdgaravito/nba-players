/** @type {import('@sveltejs/kit').Config} */
const config = {
	kit: {
		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',
		vite: {
			server: {
			  watch: {
				usePolling: true,
			  },
			},
		  }
	}
};

export default config;
