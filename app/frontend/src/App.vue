<template>
    <div id="app">
        <navbar></navbar>
        <search></search>
    </div>
</template>

<script>
import Navbar from './components/NavbarComponent';
import Search from './components/SearchComponent';

export default {
    name: 'App',
    components: {
        Navbar,
        Search,
    },
};
</script>

<style>
body {
    background-color: #71c9f8;
}
</style>
