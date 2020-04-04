<template>
    <button @click="block()" type="button" class="btn btn-danger btn-lg btn-block">
        Block all listed accounts
    </button>
</template>

<script>
import axios from 'axios';
const delay = (milisecs) => {
    return new Promise((resolve) => {
        setTimeout(resolve, milisecs);
    });
};

export default {
    name: 'blockAll',
    props: {
        profiles: {
            type: Array,
            default: null,
        },
    },
    methods: {
        async block() {
            for (const profile of this.profiles) {
                axios
                    .post(`http://localhost:5000/api/1.0/profiles/block/${profile.id}`)
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((error) => {
                        console.error(error);
                    });
                await delay(5000);
            }
        },
    },
};
</script>

<style></style>
