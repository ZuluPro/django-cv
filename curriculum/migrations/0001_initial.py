# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import curriculum.models.utils


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, verbose_name='title')),
                ('authority', models.CharField(max_length=200, verbose_name='authority')),
                ('url', models.URLField(max_length=300, verbose_name='URL', blank=True)),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='CertificationItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('start_year', models.IntegerField(verbose_name='start year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('start_month', models.IntegerField(verbose_name='start month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('expires', models.BooleanField(default=False, verbose_name='expires')),
                ('end_year', models.IntegerField(blank=True, null=True, verbose_name='end year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('end_month', models.IntegerField(blank=True, null=True, verbose_name='end month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('certification', models.ForeignKey(related_name='items', to='curriculum.Certification')),
            ],
        ),
        migrations.CreateModel(
            name='Experience',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=200, verbose_name='title')),
                ('entreprise', models.CharField(max_length=200, verbose_name='entreprise')),
                ('context', models.TextField(max_length=1000, verbose_name='context', blank=True)),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('results', models.TextField(max_length=3000, verbose_name='results', blank=True)),
                ('type', models.CharField(max_length=5, null=True, verbose_name='type', choices=[(None, 'unknown'), (b'SALAR', 'salaried'), (b'CHIEF', 'founder/chief'), (b'FREEL', 'freelance/chief'), (b'OTHER', 'other')])),
                ('environment', models.CharField(max_length=400, verbose_name='environment', blank=True)),
                ('start_year', models.IntegerField(default=curriculum.models.utils.current_year, verbose_name='start year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('start_month', models.IntegerField(default=curriculum.models.utils.current_month, verbose_name='start month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('still', models.BooleanField(default=True, verbose_name='still in office')),
                ('end_year', models.IntegerField(blank=True, null=True, verbose_name='end year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('end_month', models.IntegerField(blank=True, null=True, verbose_name='end month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('weight', models.IntegerField(default=1, verbose_name='weight', choices=[(0, 'Minor'), (1, 'Medium'), (2, 'Major')])),
            ],
        ),
        migrations.CreateModel(
            name='Language',
            fields=[
                ('name', models.CharField(max_length=50, unique=True, serialize=False, verbose_name='name', primary_key=True)),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='LanguageItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(default=b'NOT', max_length=5, verbose_name='level', choices=[(b'NOT', 'Notion'), (b'BAS', 'basic'), (b'ADV', 'advanced'), (b'PRO', 'professional'), (b'BIL', 'bilingual')])),
                ('language', models.ForeignKey(related_name='items', to='curriculum.Language')),
            ],
        ),
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(unique=True, max_length=200, verbose_name='title')),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('url', models.URLField(max_length=300, verbose_name='URL', blank=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProjectItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('contribution', models.TextField(max_length=3000, verbose_name='contribution', blank=True)),
                ('start_year', models.IntegerField(default=curriculum.models.utils.current_year, verbose_name='start year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('start_month', models.IntegerField(default=curriculum.models.utils.current_month, verbose_name='start month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('still', models.BooleanField(default=True, verbose_name='still contributor')),
                ('end_year', models.IntegerField(blank=True, null=True, verbose_name='end year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('end_month', models.IntegerField(blank=True, null=True, verbose_name='end month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('weight', models.IntegerField(default=1, verbose_name='weight', choices=[(0, 'Minor'), (1, 'Medium'), (2, 'Major')])),
                ('project', models.ForeignKey(related_name='items', to='curriculum.Project')),
            ],
        ),
        migrations.CreateModel(
            name='Resume',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('firstname', models.CharField(max_length=150, verbose_name='First name')),
                ('lastname', models.CharField(max_length=150, verbose_name='Last name')),
                ('title', models.CharField(max_length=200, null=True, verbose_name='Title', blank=True)),
                ('resume', models.TextField(help_text="Short profile's description", max_length=3000, null=True, verbose_name='resume', blank=True)),
                ('image', models.ImageField(upload_to=b'', null=True, verbose_name='image', blank=True)),
                ('phone', models.CharField(max_length=100, null=True, verbose_name='phone', blank=True)),
                ('website', models.URLField(max_length=300, null=True, verbose_name='website', blank=True)),
                ('email', models.CharField(max_length=100, null=True, verbose_name='email', blank=True)),
                ('city', models.CharField(max_length=100, null=True, verbose_name='city', blank=True)),
                ('country', models.CharField(max_length=100, null=True, verbose_name='country', blank=True)),
                ('address', models.CharField(max_length=300, null=True, verbose_name='address', blank=True)),
                ('skill_summary', models.TextField(max_length=1000, null=True, verbose_name='summary of skills', blank=True)),
                ('experience_summary', models.TextField(max_length=1000, null=True, verbose_name='summary of experience', blank=True)),
                ('training_summary', models.TextField(max_length=1000, null=True, verbose_name='summary of trainings', blank=True)),
                ('project_summary', models.TextField(max_length=1000, null=True, verbose_name='summary of projects', blank=True)),
                ('driving_license', models.CharField(max_length=100, null=True, verbose_name='driving license', blank=True)),
                ('hobbies', models.TextField(max_length=1000, null=True, verbose_name='hobbies', blank=True)),
                ('tags', models.CharField(max_length=500, null=True, verbose_name='tags', blank=True)),
                ('skype', models.CharField(max_length=100, null=True, verbose_name='Skype ID', blank=True)),
                ('twitter', models.CharField(max_length=100, null=True, verbose_name='Twitter', blank=True)),
                ('linkedin', models.CharField(max_length=100, null=True, verbose_name='LinkedIn ID', blank=True)),
                ('google', models.CharField(max_length=100, null=True, verbose_name='Google+ ID', blank=True)),
                ('stackoverflow', models.IntegerField(null=True, verbose_name='StackOverflow ID', blank=True)),
                ('github', models.CharField(max_length=300, null=True, verbose_name='GitHub ID', blank=True)),
            ],
            options={
                'verbose_name': 'resume',
            },
        ),
        migrations.CreateModel(
            name='Skill',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(unique=True, max_length=200, verbose_name='name')),
                ('description', models.TextField(max_length=2000, verbose_name='description', blank=True)),
                ('url', models.URLField(max_length=300, verbose_name='URL', blank=True)),
                ('tags', models.CharField(max_length=500, verbose_name='tags', blank=True)),
                ('color', models.CharField(max_length=50, verbose_name='color', blank=True)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='SkillItem',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('level', models.CharField(max_length=1, verbose_name='level', choices=[(None, 'unknown'), (b'B', 'beginner'), (b'S', 'skilled'), (b'A', 'advanced'), (b'E', 'expert')])),
                ('category', models.CharField(max_length=50, verbose_name='category', blank=True)),
                ('start_year', models.IntegerField(default=curriculum.models.utils.current_year, null=True, verbose_name='start year', blank=True, choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('start_month', models.IntegerField(default=curriculum.models.utils.current_month, null=True, verbose_name='start month', blank=True, choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('weight', models.IntegerField(default=1, verbose_name='weight', choices=[(0, 'Minor'), (1, 'Medium'), (2, 'Major')])),
                ('resume', models.ForeignKey(related_name='skills', to='curriculum.Resume')),
                ('skill', models.ForeignKey(related_name='items', to='curriculum.Skill')),
            ],
        ),
        migrations.CreateModel(
            name='Training',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('school', models.CharField(max_length=150, verbose_name='school')),
                ('degree', models.CharField(max_length=150, verbose_name='degree')),
                ('topic', models.CharField(max_length=150, verbose_name='topic', blank=True)),
                ('result', models.CharField(max_length=150, verbose_name='result', blank=True)),
                ('description', models.TextField(max_length=3000, verbose_name='description', blank=True)),
                ('year', models.IntegerField(verbose_name='year', choices=[(2029, 2029), (2028, 2028), (2027, 2027), (2026, 2026), (2025, 2025), (2024, 2024), (2023, 2023), (2022, 2022), (2021, 2021), (2020, 2020), (2019, 2019), (2018, 2018), (2017, 2017), (2016, 2016), (2015, 2015), (2014, 2014), (2013, 2013), (2012, 2012), (2011, 2011), (2010, 2010), (2009, 2009), (2008, 2008), (2007, 2007), (2006, 2006), (2005, 2005), (2004, 2004), (2003, 2003), (2002, 2002), (2001, 2001), (2000, 2000), (1999, 1999), (1998, 1998), (1997, 1997), (1996, 1996), (1995, 1995), (1994, 1994), (1993, 1993), (1992, 1992), (1991, 1991), (1990, 1990), (1989, 1989), (1988, 1988), (1987, 1987), (1986, 1986), (1985, 1985), (1984, 1984), (1983, 1983), (1982, 1982), (1981, 1981), (1980, 1980), (1979, 1979), (1978, 1978), (1977, 1977), (1976, 1976), (1975, 1975), (1974, 1974), (1973, 1973), (1972, 1972), (1971, 1971), (1970, 1970), (1969, 1969), (1968, 1968), (1967, 1967), (1966, 1966), (1965, 1965), (1964, 1964), (1963, 1963), (1962, 1962), (1961, 1961), (1960, 1960), (1959, 1959), (1958, 1958), (1957, 1957), (1956, 1956), (1955, 1955), (1954, 1954), (1953, 1953), (1952, 1952), (1951, 1951), (1950, 1950), (1949, 1949), (1948, 1948), (1947, 1947), (1946, 1946), (1945, 1945), (1944, 1944), (1943, 1943), (1942, 1942), (1941, 1941), (1940, 1940), (1939, 1939), (1938, 1938), (1937, 1937), (1936, 1936), (1935, 1935), (1934, 1934), (1933, 1933), (1932, 1932), (1931, 1931), (1930, 1930), (1929, 1929), (1928, 1928), (1927, 1927), (1926, 1926), (1925, 1925), (1924, 1924), (1923, 1923), (1922, 1922), (1921, 1921), (1920, 1920), (1919, 1919), (1918, 1918), (1917, 1917), (1916, 1916), (1915, 1915), (1914, 1914), (1913, 1913), (1912, 1912), (1911, 1911), (1910, 1910), (1909, 1909), (1908, 1908), (1907, 1907), (1906, 1906), (1905, 1905), (1904, 1904), (1903, 1903), (1902, 1902), (1901, 1901), (1900, 1900)])),
                ('month', models.IntegerField(verbose_name='month', choices=[(1, 'january'), (2, 'febuary'), (3, 'march'), (4, 'april'), (5, 'may'), (6, 'june'), (7, 'july'), (8, 'august'), (9, 'september'), (10, 'october'), (11, 'november'), (12, 'december')])),
                ('resume', models.ForeignKey(related_name='trainings', to='curriculum.Resume')),
            ],
        ),
        migrations.AddField(
            model_name='projectitem',
            name='resume',
            field=models.ForeignKey(related_name='projects', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='languageitem',
            name='resume',
            field=models.ForeignKey(related_name='languages', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='experience',
            name='resume',
            field=models.ForeignKey(related_name='experiences', to='curriculum.Resume'),
        ),
        migrations.AddField(
            model_name='certificationitem',
            name='resume',
            field=models.ForeignKey(related_name='certifications', to='curriculum.Resume'),
        ),
        migrations.AlterUniqueTogether(
            name='certification',
            unique_together=set([('title', 'authority')]),
        ),
        migrations.AlterUniqueTogether(
            name='skillitem',
            unique_together=set([('skill', 'resume')]),
        ),
        migrations.AlterUniqueTogether(
            name='projectitem',
            unique_together=set([('resume', 'project')]),
        ),
        migrations.AlterUniqueTogether(
            name='languageitem',
            unique_together=set([('language', 'resume')]),
        ),
        migrations.AlterUniqueTogether(
            name='certificationitem',
            unique_together=set([('certification', 'resume')]),
        ),
    ]
