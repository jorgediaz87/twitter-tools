<template>
    <button @click="blockInterval" type="button" class="btn btn-danger btn-lg btn-block">
        Block all listed accounts
    </button>
</template>

<script>
import axios from 'axios';

export default {
    name: 'blockAll',
    data() {
        return {
            lastIteration: Boolean,
        };
    },
    props: {
        profiles: {
            type: Array,
            default: null,
        },
    },
    methods: {
        blockAll() {
            this.profiles.forEach((profile, index) => {
                if (index === this.profiles.length - 1) {
                    this.lastIteration = true;
                }
                axios
                    .post(`http://localhost:5000/api/1.0/profiles/block/${profile.id}`)
                    .then((res) => {
                        console.log(res);
                    })
                    .catch((error) => {
                        console.error(error);
                    });
            });
        },
        // TODO: FIX THIS
        blockInterval() {
            console.log(this.lastIteration);
            if (!this.lastIteration) {
                setInterval(() => {
                    this.blockAll();
                }, 5000);
            } else {
                clearInterval(this.blockAll());
            }
        },
    },
};
</script>

<style></style>
